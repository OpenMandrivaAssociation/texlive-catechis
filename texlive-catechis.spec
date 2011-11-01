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
Requires(post):	texlive-tlpkg
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
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/catechis/catechis.sty
%doc %{_texmfdistdir}/doc/latex/catechis/README
%doc %{_texmfdistdir}/doc/latex/catechis/catechis.pdf
%doc %{_texmfdistdir}/doc/latex/catechis/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/catechis/catechis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
