Name:		texlive-catechis
Version:	2.0
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

%description
The macros include: - format for question-and-answer; -
comments on answers; - citations; - a specialised enumerate
which only operates in the catechism parts of a document. The
macros are all highly customisable.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/catechis
%doc %{_texmfdistdir}/doc/latex/catechis
#- source
%doc %{_texmfdistdir}/source/latex/catechis

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
