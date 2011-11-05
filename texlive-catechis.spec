# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/catechis
# catalog-date 2008-09-02 21:23:27 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-catechis
Version:	1.1
Release:	1
Summary:	Macros for typesetting catechisms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/catechis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The macros include: - format for question-and-answer; -
comments on answers; - citations; - a specialised enumerate
which only operates in the catechism parts of a document. The
macros are all highly customisable.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/catechis/catechis.sty
%doc %{_texmfdistdir}/doc/latex/catechis/README
%doc %{_texmfdistdir}/doc/latex/catechis/catechis.pdf
%doc %{_texmfdistdir}/doc/latex/catechis/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/catechis/catechis.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
